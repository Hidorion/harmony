$(document).ready(function(){
    if (document.getElementsByClassName("index") !== null) {
        let imgList = document.getElementsByClassName("img-src");
        let imgToChange = document.getElementsByClassName("img-gallery");
        let currentPosition = 0;
        /**
         * Change the images from the right to the left side.
         */
        function changeImages() {
            currentPosition++;
            for (let i = 2; i >= 0; i--) {
                let pos = currentPosition + i
                pos = pos % imgList.length;
                updateImage(i, pos);
            }
        }
        /**
         * Update the images with changing the src, alt and title of the img tag.
         * @param i is the position of the image to modify.
         * @param position is the position where the new values are stored.
         */
        function updateImage(i, position) {
            imgToChange[i].src = imgList[position].src;
            imgToChange[i].alt = imgList[position].alt;
            imgToChange[i].title = imgList[position].title;
            document.getElementsByClassName("div-img-menu")[i].textContent = imgList[position].title;
            document.getElementsByClassName("a-title")[i].href = "gallery#" + imgList[position].id;    
        }

        changeImages();

        setInterval(function () {
            changeImages();
        }, 3000)
    }
});
