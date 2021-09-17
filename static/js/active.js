function render_category(id){
    console.log("Category...",id)
    url = '/category/'
    fetch(url,{
    method:'GET',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    })
    .then((response)=>{
    response.json().then((data) => {
        console.log(data)
        html = ''
        // for(i=0;i<data.datas.length;i++){
        //     html += `
        //         <div class="col-sm-6 col-md-4 ">
        //             <div class="box ">
        //                 <div class="img-box">
        //                     <img src="" alt="">
        //                 </div>
        //                 <div class="detail-box">
        //                     <h5>
        //                       Textbooks
        //                     </h5>
        //                     <p>
        //                       fact that a reader will be distracted by the readable content of a page when looking at its layout.
        //                       The
        //                       point of using
        //                     </p>
        //                 </div>
        //             </div>
        //         </div>
        //     `
        // }
        // document.getElementById('category').innerHTML = html

       })
    })
}