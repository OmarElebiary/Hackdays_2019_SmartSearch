$("#searchForm").submit((e) => {
    e.preventDefault();
});

function search() {
    console.log('Searching the database');
    let searchTerm = document.querySelector("#searchTerm").value;
    console.log(searchTerm);
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState == XMLHttpRequest.DONE) console.log(xhr.responseText);
    };
    xhr.open('POST', 'http://localhost:5000/', true);
    xhr.send(searchTerm);
    for(var i = 0;i < 4;i++)
        insertResultRow('result_' + i);
}

let insertResultRow = ((data) => {
    var resultRow = document.createElement("div");
    resultRow.innerHTML = `
        <div style="margin-top: 20px">
        <div class="card" onclick="showResult('${data}')">
            <div class="card-body">
            <h5 class="card-title"><a href="">filename</a></h5>
            ${data}
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
        <img class="card-img-top" src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22286%22%20height%3D%22180%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20286%20180%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_168f5850f7b%20text%20%7B%20fill%3Argba(255%2C255%2C255%2C.75)%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A14pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_168f5850f7b%22%3E%3Crect%20width%3D%22286%22%20height%3D%22180%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22107.1953125%22%20y%3D%2296.6%22%3E286x180%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E" alt="file thumbnail">  
        <div class="card-body">
            <h5 class="card-title">Filename</h5>
            ${data}
        </div>
    </div>
    </div>`;
}