var time = $('#myDiv').val();     // = "Mon Nov 07 2011 06:41:48 GMT-0500 (Eastern Standard Time)";
var timeObject = new Date(time);                
alert(timeObject);
timeObject.setSeconds(timeObject.getSeconds() + 60);    
alert(timeObject);