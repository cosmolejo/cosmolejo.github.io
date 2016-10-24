<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>index.html</title>
    </head>
    <body>
        <center>
            <h1>Tabla periodica</h1>
        <table border=1px style='border-collapse: collapse;border:solid black 0px;'>

        <?php

            $elements = array(); //arreglo del archivo
            $file = fopen("ElementosQuimicos.txt", "r");
            while (!feof($file) )
            {
                $line = fgets($file);
                $elements[] = explode(',', $line);
            }

            fclose($file);
           /*
            
             //Diccionario 
            $elementos=array("0"=>"",
                                "1"=>array("simbolo"=>"H","nombre"=>"Hidrogeno"),
                                "2"=>array("simbolo"=>"He","nombre"=>"Helio"),
                                "3"=>array("simbolo"=>"Li","nombre"=>"Litio")
                            );


            $simbolo=$elementos[1]["simbolo"];
            $nombre=$elementos[1]["nombre"];
            */    
            $blancos=array("0"=>array(),
	      "1"=>array(2,17),
	      "2"=>array(3,12),
	      "3"=>array(3,12),
	      "4"=>array(0,0),
	      "5"=>array(0,0),
	      "6"=>array(0,0),
	      "7"=>array(0,0));

            $Z=0;
            for($i=1;$i<=7;$i++){
            echo "<tr>";
            $limites=$blancos[$i];
            $minimo=$limites[0];
            $maximo=$limites[1];
            
                        
            for($j=1;$j<=18;$j++){
	
                if($j<$minimo or $j>$maximo){
                                	    $Z++;
                                            $simbolo=$elements[$Z][1];
                                            $nombre=$elements[$Z]["0"];
                                            echo "

                                                    <td style='border:solid black 1px;'>
                                                    <div style='float:right'>$Z</div>
                                                    <big>$simbolo</big><br/>
                                                    $nombre
                                                    </td>

                                                ";
                                            }else{
                                                    echo "<td style='border:solid black 0px;'></td>";
                                                 }
                                    }
                                            echo "</tr>";
                                }       

        ?>

        </table>
        </center>
    </body>
</html>