function category_product(id){
    console.log(id)
    url = `/product_category/`
    fetch(url,{
    method:'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({
        'category':id,
    })
    })
    .then((response)=>{
    response.json().then((data) => {
        console.log(data)
        html = `
                <div class="col-md-12 " style="margin-bottom: 20px">
                    <div class="overview-wrap">
                        <h2 class="title-1"></h2>
                        <button type="button" style="border-color: black" class="btn btn-secondary mb-1" data-toggle="modal" data-target="#AddModal">
                        <i class="zmdi zmdi-plus"></i>
                            Add element
                        </button>
                    </div>
                </div>
        `
        for(let i=0; i<data.data.length;i++) {
            html += `
                <div class="col-sm-4 col-lg-4">
                    <div class="overview-item overview-item--c1">
                        <div class="overview__inner">
                            <div class="overview-box clearfix">
                                <div class="icon">
                                    <img class="image-tag" src="${ data.data[i].image }">
                                </div>
                                <div class="text">
                                    <h4>${ data.data[i].name }</h4>
                                </div>
                            </div>
                            <div class="overview-chart">
                                <canvas id="widgetChart1"></canvas>
                            </div>
                        </div>
                    </div>
                </div>         `
        }
        document.getElementById('category').innerHTML = html
       })
    })
}

function save(){
    url = `/save/`
    // file = document.getElementById('file-multiple-input').files
    fileList = ''
    const fileSelector = document.getElementById('file-multiple-input');
        fileSelector.addEventListener('change', (event) => {
        fileList = event.target.files;
        console.log(fileList);
    });
    fetch(url,{
    method:'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({
        'file':fileList,
    })
    })
    .then((response)=>{
    response.json().then((data) => {

      console.log(data)
   })
   })
}
