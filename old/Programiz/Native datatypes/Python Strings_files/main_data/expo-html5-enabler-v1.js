var srt= window.location.href;
var EXclickArr = [];
var EXimpArr = [];
		
		
 if(srt.split("=").length!=1){
		var _$CLICK$ = unescape(srt.split("=")[1].split("&")[0]);
		// ---------- Collecting all clickTags from Query string-----------
			var _clickTags= srt.split("&")[1];
			 for(var ct=0; ct<srt.split("&")[1].split(",").length; ct++){
			 
			 var ctString = unescape(srt.split("&")[1].split(",")[ct].substring(srt.split("&")[1].split(",")[ct].search("http"), srt.split("&")[1].split(",")[ct].length));
			  if(_$CLICK$!=undefined && _$CLICK$!="$CLICK$"){
			      ctString = _$CLICK$+ctString;
			   }
			   EXclickArr.push(ctString);
			  }
			 window.EXcta = EXclickArr;
			 
			 window.EXclickTag = function(_id){
				if((srt.split("=").length!=1)){
				 	var _totalCTA =srt.split("&")[1].split(",").length;
			          if(((_id)<=_totalCTA)){
						window.open( window.EXcta[(_id-1)] , "_blank");
				      }
			else{console.log("\nclickTag"+_id+ " NOT DEFINED IN index.html!\n\n")}
			}else{console.log("Please check banner via index.html file. Because all click through URL has been defined there.")}
			  		 
			 }



			 
			  
	// ---------- Collecting all impTags from Query string-----------
			var _imp = srt.split("&");
			for(var a=0; a<_imp[2].split(",").length; a++){
			 EXimpArr.push(unescape(_imp[2].split(",")[a].substring(_imp[2].split(",")[a].search("http"), _imp[2].split(",")[a].length)));
			}
			window.impTag = EXimpArr;
			
			
			 window.EXtrackImp = function(_id){
			  
			 if((srt.split("=").length!=1)){
				 	var _totalIMP =srt.split("&")[2].split(",").length;
			          if(((_id)<=_totalIMP)){
				 		var img = new Image();
		         			img.src= window.impTag[_id-1];
							console.log("imp"+(_id)+" = "+ window.impTag[_id-1]);
				 	   }else{console.log("\nimpTag"+_id+ " NOT DEFINED IN index.html! Please define to avoid unexpected response\n\n")}
			}else{
				console.log("Please check banner via index.html file. Because all 1x1 imp URL has been defined there.");
			}
			  
			}
			console.log("clickTag Info "+(window.EXcta))
			
			
  }
			
			 	
			
			
 