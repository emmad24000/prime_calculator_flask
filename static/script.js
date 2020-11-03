        function input(){
            var slider = document.getElementById("slider");
            var current = document.getElementById("current");
            current.innerHTML = slider.value;

        }
        function submit(){
            var link = document.getElementById("link");
            var slider = document.getElementById("slider");

            var current = slider.value;
            link.href = "/isPrime/"+current;

        }
