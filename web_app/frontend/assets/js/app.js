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
            console.log(xhr.responseText);
            document.getElementById('loading').style.display = 'none';
            let result = JSON.parse(xhr.response);
            console.log(xhr.responseText.length);
            for(var i = 0;i < result.length;i++)
                insertResultRow(result[i]);                
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
            <p>File description</p>
            <p>File category</p>
            </div>
        </div>
    </div>`;
    document.getElementById('resultsContainer').appendChild(resultRow);
});

function clearResults() {
    let node = document.getElementById('resultsContainer');
    node.innerHTML = '';
}

function showResult(data) {
    let node = document.getElementById('resultPreview');
    console.log(data);
    node.innerHTML = data;
    node.innerHTML = `
        <div style="margin-top: 20px;">
        <div class="card">
        
        <embed src="http://localhost:5000/file/${data}#toolbar=0" type="application/pdf" class="card-img-top" width="100%" height="600px" />
        <div class="card-body">
            
            <h5 class="card-title">Filename</h5>
            ${data}
        </div>
    </div>
    </div>`;
}

function fileViewGenerator(filename) {
    let ext = filename.substring(filename.lastIndexOf('.') + 1, filename.length);
    return ext;
}