// window.addEventListener('resize', resize_menu_lateral);
window.addEventListener('resize', resize_menu_carrito);

// var estado_find = false

// var estado_menu_favoritos = false
// var pageWidth = 0;

// var menuFavoritos = document.getElementById("menu-favoritos")
// var fav_btn = document.getElementById("favorite-btn")
// var find = document.getElementById("find")
var estado_menu_carrito = false
var menuCarrito = document.getElementById("menu-carrito")


// function manejarMenuOpciones() {
//     if (estado_menu_lateral) {
//         linea1.classList.remove("rotate");
//         linea1.classList.add("a-rotate");

//         linea2.classList.remove("rotate-2");
//         linea2.classList.add("a-rotate-2");

//     } else {
//         if (estado_find) {
//             ocultarFind();
//         }
//         linea1.classList.remove("a-rotate");
//         linea1.classList.add("rotate");

//         linea2.classList.remove("a-rotate-2");
//         linea2.classList.add("rotate-2");

//         menuCarrito.style.left = "0";
//     }
//     estado_menu_lateral = !estado_menu_lateral
//     resize_menu_lateral()
// }


function manejarMenuCarrito(){
    estado_menu_carrito = !estado_menu_carrito
    resize_menu_carrito()
}


// function resize_menu_lateral() {
//     pageWidth = document.documentElement.scrollWidth;
//     if (!estado_menu_lateral) {
//         if (pageWidth < 600) {
//             menuCarrito.style.left = "-41vw";
//         } else if (pageWidth < 900) {
//             menuCarrito.style.left = "-51vw";
//         } else {
//             menuCarrito.style.left = "-31vw";
//         }
//     } else {
//         menuCarrito.style.left = "0";
//         if (pageWidth < 600) {
//             menuCarrito.style.width = "41vw";
//         } else if (pageWidth < 900) {
//             menuCarrito.style.width = "51vw";
//         } else {
//             menuCarrito.style.width = "31vw";
//         }
//     }
// }

function resize_menu_carrito() {
    pageWidth = document.documentElement.scrollWidth;
    if (!estado_menu_carrito) {
        if (pageWidth < 600) {
            menuCarrito.style.right = "-41vw";
        } else if (pageWidth < 900) {
            menuCarrito.style.right = "-51vw";
        } else {
            menuCarrito.style.right = "-31vw";
        }
    } else {
        menuCarrito.style.right = "0";
        if (pageWidth < 600) {
            menuCarrito.style.width = "46vw";
        } else if (pageWidth < 900) {
            menuCarrito.style.width = "36vw";
        } else {
            menuCarrito.style.width = "28vw";
        }
    }
}







// function ocultarFind() {
//     if (estado_find) {
//         find.classList.remove("find-show");
//         find.classList.add("find-hidden");
//     } else {
//         find.classList.remove("find-hidden");
//         find.classList.add("find-show");
//         if (estado_menu_lateral) {
//             manejarMenuOpciones()

//         }

//         if(estado_menu_favoritos){
//             manejarMenuFavoritos()
//         }
//     }
//     estado_find = !estado_find
// }




// var top_header_seleccionado = 1

// setInterval(actualizar_top_header, 6000);
// const div1 = document.getElementById("top-header-content-1");
// const div2 = document.getElementById("top-header-content-2");
// const div3 = document.getElementById("top-header-content-3");

// function actualizar_top_header() {
//     switch (top_header_seleccionado) {
//         case 1:
//             div1.style.top = "-50px";
//             div2.style.top = "1vh";
//             top_header_seleccionado++;
//             break;
//         case 2:
//             div2.style.top = "-50px";
//             div3.style.top = "1vh";        
//             top_header_seleccionado++;
//             break;
//         case 3:
//             div3.style.top = "-50px";
//             div1.style.top = "1vh";
//             top_header_seleccionado=1;
//             break;
//     }

// }
