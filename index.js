async function loadModel() {
    const model = await tf.loadLayersModel('tfjs_model/model.json');
    console.log("Model Loaded Successfully!");
}
loadModel();
