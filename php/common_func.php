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

//和后面的getTagsFromString组成开头-结尾式的字符串截取.
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

//utf-16 urlencode方式
function utf16urlencode($str){
    $str = mb_convert_encoding($str, 'UTF-16LE', 'UTF-8');
    $out = '';
	$outarray = array();
    for ($i = 0; $i < mb_strlen($str, 'UTF-16LE'); $i++){
		$strtmp = bin2hex(mb_substr($str, $i, 1, 'UTF-16LE'));
        $outarray[] = '%'.substr($strtmp,0,2).'%'.substr($strtmp,2,2);
    }
	$returnstr = implode('', $outarray);
	return $returnstr;
}

//从数据array画一个表格
function draw_table_body($table_data, $table_class, $table_head = '', $odd_tr_class = ''){
	$return_str = '<table class="'.$table_class.'">';
	//处理table_head为array的情况.
	if(is_array($table_head)){
		$addstr = implode("</td><td>", $table_head);
		if($addstr){
			$return_str = $return_str.'<tr>';
			$return_str = $return_str.'<td>'.$addstr.'</td>';
			$return_str = $return_str.'</tr>';
		}
	}else{
		$return_str = $return_str.$table_head;
	}
	$return_str = $return_str.'<tbody>';
	$line_count = 0; //算奇偶的
	foreach ($table_data as $row){
		++$line_count;
		$my_tr_class = '';
		if($line_count % 2 != 0){
			$my_tr_class = $odd_tr_class;
		}
		$return_str = $return_str.'<tr class="'.$odd_tr_class.'">';
		foreach ($row as $field){
			$return_str = $return_str.'<td>'.$field.'</td>';
		}
		$return_str = $return_str.'</tr>';
	}
	$return_str = $return_str.'</tbody></table>';
	return $return_str;
}


?>