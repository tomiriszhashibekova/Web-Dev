var taskInput=document.getElementById("new-task");
var addButton=document.getElementsByTagName("button")[0];
var incompleteTaskHolder=document.getElementById("incomplete-tasks");
var completedTasksHolder=document.getElementById("completed-tasks");



var createNewTaskElement=function(taskString){

	var listItem=document.createElement("li");

	
	var checkBox=document.createElement("input");
	
	var label=document.createElement("label");
	
	var editInput=document.createElement("input");
	
	var deleteButton=document.createElement("button");

	label.innerText=taskString;

	
	checkBox.type="checkbox";
	
	deleteButton.innerText="Delete";
	deleteButton.className="delete";



	
	listItem.appendChild(checkBox);
	listItem.appendChild(label);
	
	listItem.appendChild(deleteButton);
	return listItem;
}



var addTask=function(){
	console.log("Add Task...");
	
	var listItem=createNewTaskElement(taskInput.value);

	
	incompleteTaskHolder.appendChild(listItem);
	bindTaskEvents(listItem, taskCompleted);

	taskInput.value="";

}


var deleteTask=function(){
		console.log("Delete Task...");

		var listItem=this.parentNode;
		var ul=listItem.parentNode;
		
		ul.removeChild(listItem);

}



var taskCompleted=function(){
		console.log("Complete Task...");
	    
	
	var listItem=this.parentNode;
	completedTasksHolder.appendChild(listItem);
				bindTaskEvents(listItem, taskIncomplete);

}




var ajaxRequest=function(){
	console.log("AJAX Request");
}


addButton.onclick=addTask;

addButton.addEventListener("click",ajaxRequest);


var bindTaskEvents=function(taskListItem,checkBoxEventHandler){
	console.log("bind list item events");

	var checkBox=taskListItem.querySelector("input[type=checkbox]");
	
	var deleteButton=taskListItem.querySelector("button.delete");


			
			deleteButton.onclick=deleteTask;
			
			checkBox.onchange=checkBoxEventHandler;
}


for (var i=0; i<completedTasksHolder.children.length;i++){
	
		bindTaskEvents(completedTasksHolder.children[i],taskIncomplete);
		

	}
