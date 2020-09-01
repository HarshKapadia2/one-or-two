const MAX_VIDEO_WIDTH = 480;

let
	video,
	cameraAction,
	
	canvas,
	g,
	
	imageUpload
;

window.addEventListener("load", () => {
	video = document.querySelector("#CameraDisplay");
	canvas = document.querySelector("#CanvasDisplay");
	
	cameraAction = document.querySelector("#CameraAction");
	cameraAction.addEventListener("click", () => {
		if(cameraAction.classList.contains("captureImage"))
			captureImage();
		else
			accessCamera()
				.then(() => cameraAction.classList.add("captureImage"))
				.catch(() => document.querySelector("#PermissionError").classList.remove("hide"));
	});
	
	imageUpload = document.querySelector("#image-upload");
});

async function accessCamera(){
	video.srcObject = await navigator.mediaDevices.getUserMedia({
		video: {
			facingMode: "user",
			width: 9999,
			height: 9999
		}
	});
	
	video.play();
	
	video.addEventListener("canplay", () => {
		let width = video.videoWidth;
		let height = video.videoHeight;
		
		//video.width = width;
		//video.height = height;
		
		canvas.width = width;
		canvas.height = height;
		g = canvas.getContext("2d");
	});	
}

function dataUrltoFile(dataurl, filename) {
	let arr = dataurl.split(","),
		bstr = atob(arr[1]),
		u8arr = new Uint8Array(bstr.length);
	
	for(let i = 0; i < bstr.length; i++)
		u8arr[i] = bstr.charCodeAt(i);
	
	return new File([u8arr], filename, {type: arr[0].match(/:(.*?);/)[1]});
}

function dataURLtoFile(dataurl, filename) {

	var arr = dataurl.split(','),
		mime = arr[0].match(/:(.*?);/)[1],
		bstr = atob(arr[1]), 
		n = bstr.length, 
		u8arr = new Uint8Array(n);
		
	while(n--){
		u8arr[n] = bstr.charCodeAt(n);
	}
	
	return new File([u8arr], filename, {type:mime});
}

function captureImage(){
	if(!g)
		return;
	
	g.drawImage(video, 0, 0);
	
	let dt = new DataTransfer();
	dt.items.add(new dataURLtoFile(canvas.toDataURL("image/jpg"), "image.jpg"))
	imageUpload.files = dt.files;
}
