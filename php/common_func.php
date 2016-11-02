<?php 

/* gets the data from a URL */
function get_data($url) {
	$ch = curl_init();
	$timeout = 5;
	curl_setopt($ch,CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0');
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
	$data = curl_exec($ch);
	curl_close($ch);
	return $data;
}

function getTagFromString($input, $startTag, $endTag, $detect = ''){
	$rs = getTagsFromString($input, $startTag, $endTag, $detect);
	if(!isset($rs[0])){
		return false;
	}else{
		return $rs[0];
	}
}

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