// JavaScript Code from Cloudinary for the Cloudinary widget
var myWidget = cloudinary.createUploadWidget({
    cloudName: 'joyzadan',
    uploadPreset: 'efjhsjfdjrdnrhlk'
}, (error, result) => {
    if (!error && result && result.event === "success") {
        console.log('Done! Here is the image info: ', result.info);
    }
})

document.getElementById("upload_widget").addEventListener("click", function () {
    myWidget.open();
}, false);