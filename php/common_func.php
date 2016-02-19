<?php 

function getTagsFromString($input, $startTag, $endTag, $detect = ''){
		
		$result = array();
		$startTagPos = 0;
		$endTagPos = 0;
		$catchFlag = false;
		while(true){
			$startTagPos = strpos($input, $startTag, $startTagPos);
			if($startTagPos === false){
				break; //exit when not found
			}
			$endTagPos = strpos($input, $endTag, $startTagPos + strlen($startTag));
			if($endTagPos === false){
				break;
			}
			$getlen = $endTagPos - ($startTagPos + strlen($startTag)); //strlen(content_of_this_tag)
			$tobeAdd = substr($input, $startTagPos + strlen($startTag), $getlen);
			$startTagPos = $endTagPos + strlen($endTag); //update startpos
			if($detect && !strpos($tobeAdd, $detect, 0)){
				continue;
			}
			$result[] = $tobeAdd;
		}
		return $result;
}

?>