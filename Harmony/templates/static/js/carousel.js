document.addEventListener("DOMContentLoaded", (event) => {
    if (document.getElementsByClassName("index") !== null || document.getElementById("gallery") !== null) {
        let imgList = document.getElementsByClassName("img-src");
        // let idList = document.getElementsByClassName("get-id");
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
            document.getElementsByClassName("img-gallery")[i].src = imgList[position].src;
            document.getElementsByClassName("img-gallery")[i].alt = imgList[position].alt;
            document.getElementsByClassName("img-gallery")[i].title = imgList[position].title;
            // if (document.getElementById("references_page") !== null ){
            document.getElementsByClassName("div-img-menu")[i].textContent = imgList[position].title;
            //     document.getElementsByClassName("span-name")[i].textContent = imgList[position].alt;
            // }    
        }

        changeImages();

        setInterval(function () {
            changeImages();
        }, 3000)
    }
});
