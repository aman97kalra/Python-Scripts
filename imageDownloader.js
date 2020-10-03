const fs = require('fs');
const https = require('https');

/**
 * @param {*} url url of the image to be downloaded
 * @param {*} path path where the image is be saved.
 */
function saveImageToDisk( { url, path } ){
    var fullUrl = url;
    var localPath = fs.createWriteStream(path);
    try{
        var request = https.get( fullUrl, ( response ) => {
        //console.log(response);
        response.pipe(localPath);
        });
    } catch( e ) {
        console.log( 'error', e );
    }
};

saveImageToDisk( { url: 'https://random.dog/vh7i79y2qhhy.jpg', path: './image.jpg' } );
