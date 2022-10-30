const apiURL = 'https://amhep.pythonanywhere.com';

function fetchGrades() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        document.getElementById("grades").innerHTML = this.responseText;
    };
    xhttp.open("GET", apiURL+"/grades", true);
    xhttp.send();
}

function fetchStudentGrade () {
    var xhttp = new XMLHttpRequest();

    var name = document.getElementById("text1").value;

    xhttp.onreadystatechange = function() {
        document.getElementById("studentGrades").innerHTML = this.responseText;
    };
   
    xhttp.open("GET", apiURL + "/grades/"+ name, true);//Parse the string
    xhttp.send();
}

function newStudentGrade() {
    var xhttp = new XMLHttpRequest();
    
    xhttp.open("POST", apiURL + "/grades");
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");


    var name = document.getElementById("text2").value;
    var grade = document.getElementById("text3").value;

    xhttp.onload = function() {
        document.getElementById("newStudentGrade").innerHTML = this.responseText;
    };
    
    const body = {"name": name, "grade": grade};
    xhttp.send(JSON.stringify(body));
}

function gradeChange () {
    var xhttp = new XMLHttpRequest();

    var name = document.getElementById("text4").value;
    var grade = document.getElementById("text5").value;

    const body = {"name": name, "grade": grade};
    var json = JSON.stringify(body)

    xhttp.open("PUT", apiURL + "/grades/"+ name, true);
    xhttp.setRequestHeader("Content-Type", "application/json; charset=UTF-8");

    xhttp.onload = function() {
        document.getElementById("newGrade").innerHTML = this.responseText;
    }
    xhttp.send(json);
}

function deleteStudentGrade () {
    var xhttp = new XMLHttpRequest();

    var name = document.getElementById("text6").value;
    var grade =  document.getElementById("text7").value;

    const body = {"name": name, "grade": grade}
    var json = JSON.stringify(body);

    xhttp.open("DELETE", apiURL + "/grades/" + name, true);
    xhttp.onload = function () {
        document.getElementById("deleteStudentGrade").innerHTML = this.responseText;
    }
    xhttp.send(null);
}