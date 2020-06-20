
var firebaseConfig = { //This part connects javascript to my firebase data base, under rule 9 of the brief instructions, data stored in a password protected cloud service ...
						// is not expected that access is to be given to the examiner.
    apiKey: "AIzaSyC4CerXS2sj0KF9bK6s4dCNd-E7YZKIyNI",
    authDomain: "school-a4807.firebaseapp.com",
    databaseURL: "https://school-a4807.firebaseio.com",
    projectId: "school-a4807",
    storageBucket: "school-a4807.appspot.com",
    messagingSenderId: "765471220876",
    appId: "1:765471220876:web:ba4c60ab373669c5d3c7a9"
  };
  firebase.initializeApp(firebaseConfig);



  
  var myDB = firebase.database().ref("comments"); //variable that accesses firebase database, specifically the "comments" directory 

  //this section display the firebase content
  myDB.on("child_added", function(data, prevChildKey) { //variable uses "on" method to listen for data changes (new data) at a particular location, specifically data added ("child_added")
														//and the previous child's key to compare														
    var dataPoint = data.val(); //this variable extracts a JavaScript value from a DataSnapshot, a DataSnapshot is data from the Database location.
    var tableS = document.getElementById("myStudentTable").innerHTML; //variable that gets content from the HTML text box for commenting
    tableS += "<tr><td>" + dataPoint.name; //puts cell around data point, cell is to contain the data on a table. ".name" method is actual data content, if removed would show [object Object]
    document.getElementById("myStudentTable").innerHTML = tableS; //adds data point cell to table
  });
  
//This section sends and receives the comment box/text box inputs
  function AddComment() { //creates function
    var nameData = document.getElementById("nameIn").value; //variable that stores value or data type of what was inputed into the text box

    var myDB = firebase.database().ref(); //variable that accesses firebase database, accessing the root directory which is the first or top level directory, everything else comes after
    var sendData = myDB.child("comments").push(); //variable that "pushes"/ sends data to firebase using "push" method, sends data through child path which is inside root directory
    sendData.set({ //sets out Json format which is the layout of data in the database 
      name: nameData, //in firebase data base sent data appears as "name : [actual data content]"
    });

    document.getElementById("nameIn").value = ""; //returns the element of specified id, to get the value of the input value.

  }








 function graph() {
    var img = document.getElementById("image");
    img.src = this.value;
    return false;
}
document.getElementById("CarList").onchange = graph;



function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

