


var Pages_StartingPosition = 0;

var slideShow = document.getElementsByClassName("SCREEN_PUBLICFACE_PAGES");

function changePublicFace(SlideDirection){

	if(SlideDirection=="LEFT"){
		Pages_StartingPosition++;
	}else if(SlideDirection=="RIGHT"){
		Pages_StartingPosition--;
	}
	
	if(Pages_StartingPosition>=NumberOfPages){
		Pages_StartingPosition=0;
	}else if(Pages_StartingPosition<0){
		Pages_StartingPosition=NumberOfPages-1;
	}

	var i;
	for(i=0;i<slideShow.length;i++){
		slideShow[i].style.left= (i-Pages_StartingPosition)*100+"vw";
	}
	
}

