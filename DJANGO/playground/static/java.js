import ThisPersonDoesNotExist from 'thispersondoesnotexist-js';

const dnte = new ThisPersonDoesNotExist();

dnte.getImage().then(res  => {
	console.log('result->', res);
}).catch(err  => {
	console.log('error->', err);
});

dnte.getImage({
	width: 256, // width of the image (default 128)
	height: 256, // high of the image (default 128)
	type: 'file',  // Type of file to generate (file or base64) (default file)
	path: 'avatars' // Path to save (Applies to type file) (default .)
}).then(res  => {
	console.log('result->', res);
	/*
	{ 
		status: true,
		data:{ 
			format: 'jpeg',
			width: 256,
			height: 256,
			channels: 3,
			premultiplied: false,
			size: 9575,
			name: 'Q2m4yrR9Is.jpeg' 
		}
	}
	*/
}).catch(err  => {
	console.log('error->', err);
});