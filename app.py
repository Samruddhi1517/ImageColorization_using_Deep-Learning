from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load model
proto = "colorization_deploy_v2.prototxt"
model = "colorization_release_v2.caffemodel"
pts = "pts_in_hull.npy"

net = cv2.dnn.readNetFromCaffe(proto, model)
pts = np.load(pts)

class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")

pts = pts.transpose().reshape(2,313,1,1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1,313],2.606,dtype="float32")]

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Upload Route
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    img = cv2.imread(path)

    scaled = img.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    L = lab[:,:,0]
    L -= 50

    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0,:,:,:].transpose((1,2,0))

    ab = cv2.resize(ab,(img.shape[1],img.shape[0]))

    L += 50
    colorized = np.concatenate((L[:,:,np.newaxis],ab),axis=2)

    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized,0,1)

    output = os.path.join(OUTPUT_FOLDER,"result.jpg")
    cv2.imwrite(output,(colorized*255).astype("uint8"))

    return send_file(output,mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)