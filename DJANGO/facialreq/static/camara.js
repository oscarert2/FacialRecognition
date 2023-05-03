let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let click_button = document.querySelector("#click-photo");
let canvas = document.querySelector("#canvas");
let stop_camera_button = document.querySelector("#stop-camera");
let stream;

camera_button.addEventListener('click', async function() {
   	stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
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
    // capture the image and save it in the canvas
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    let image_data_url = canvas.toDataURL('image/jpeg');
    // data url of the image
    console.log(image_data_url);

    // get the CSRF token
    let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    $.ajax({
        url: '/save_image/',
        method: 'POST',
        data: {
            'image_data': image_data_url,
            'csrfmiddlewaretoken': csrf_token // include the CSRF token in the request data
        },
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
});
