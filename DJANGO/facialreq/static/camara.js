let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let click_button = document.querySelector("#click-photo");
let canvas = document.querySelector("#canvas");
let stop_camera_button = document.querySelector("#stop-camera");

camera_button.addEventListener('click', async function() {
   	let stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
	video.srcObject = stream;
});

stop_camera_button.addEventListener('click', function() {
	if (stream) {
        stream.getTracks().forEach(track => {
            track.stop();
        });
        video.srcObject = null;
    }
});

click_button.addEventListener('click', function() {
   	canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
   	let image_data_url = canvas.toDataURL('image/jpeg');
   	// data url of the image
   	console.log(image_data_url);
});