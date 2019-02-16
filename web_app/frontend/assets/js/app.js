$("#searchForm").submit((e) => {
    e.preventDefault();
});

function search() {
    console.log('Searching the database');
    clearResults();
    document.getElementById('loading').style.display = 'block';
    let searchTerm = document.querySelector("#searchTerm").value;
    console.log(searchTerm);
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState == XMLHttpRequest.DONE) 
        {
            document.getElementById('loading').style.display = 'none';
            let result = JSON.parse(xhr.response);
            if (result.length > 0) {
                for(var i = 0;i < result.length;i++)
                    insertResultRow(result[i]);
                showResult(result[0]);
                console.log(result);
            } else {
                showNoResults();
            }
        }
    };
    xhr.open('POST', 'http://localhost:5000/', true);
    xhr.send(searchTerm);
}

let insertResultRow = ((data) => {
    var resultRow = document.createElement("div");
    resultRow.innerHTML = `
        <div style="margin-top: 20px">
        <div class="card" onclick="showResult('${data}')">
            <div class="card-body">
            <h5 class="card-title"><a href="http://localhost:5000/file/${data}">${data}</a></h5>
            <button class="btn btn-success card-link" onclick="showResult(${data})"><i class="fas fa-file"></i> Show file</button>            
            </div>
        </div>
    </div>`;
    document.getElementById('resultsContainer').appendChild(resultRow);
});

function clearResults() {
    let resultsContainer = document.getElementById('resultsContainer');
    resultsContainer.innerHTML = '';
    let resultPreview = document.getElementById('resultPreview');
    resultPreview.innerHTML = '';
}

function showResult(data) {
    let node = document.getElementById('resultPreview');
    console.log(data);
    node.innerHTML = data;
    let viewerBody = fileViewGenerator(data);
    node.innerHTML = `
        <div style="margin-top: 20px;">
        <div class="card">      
        ${viewerBody}
        <div class="card-body">           
            <h5 class="card-title">Filename</h5>
            ${data}
            <a href="http://localhost:5000/file/${data}" class="btn btn-primary float-right card-link"><i class="fas fa-file-download"></i> Download</a>
        </div>
    </div>
    </div>`;
}

function fileViewGenerator(filename) {
    let ext = filename.substring(filename.lastIndexOf('.') + 1, filename.length);
    console.log(filename);
    console.log(ext);
    let htmlEle = '';
    if (ext === 'txt') {
        htmlEle = `<object data="http://localhost:5000/file/${filename}" type="text/plain" class="card-img-top" width="100%" style="height: 100%"></object>`;
    } else if (ext === 'pdf') {
        htmlEle = `<embed src="http://localhost:5000/file/${filename}#toolbar=0" type="application/pdf" class="card-img-top" width="100%" height="100%" />`;
    } else if (ext === 'xlsx' || ext === 'xls') {
        htmlEle = `<h4 class="card-img-top">Preview not available</h4>`;
    } else if (ext == 'jpg' || ext == 'jpeg') {
        return `<img class="card-img-top" src="http://localhost:5000/file/${filename}" alt="image search result">`;
    }
    return htmlEle;
}

function showNoResults() {

}