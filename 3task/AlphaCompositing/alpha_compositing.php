<?php
$f = 'f.png';
$b = 'b.png';
$m = 'm.png';

$im_f = imagecreatefrompng($f);
$im_b = imagecreatefrompng($b);
$im_m = imagecreatefrompng($m);

list($wf, $hf) = [imagesx($im_f),  imagesy($im_f)];
list($wb, $hb) = [imagesx($im_b),  imagesy($im_b)];
list($wm, $hm) = [imagesx($im_m),  imagesy($im_m)];
echo 'W: ' . $wf . ' H: ' . $hf . "\n";
echo 'W: ' . $wb . ' H: ' . $hb . "\n";
echo 'W: ' . $wm . ' H: ' . $hm . "\n";

$im_out = imagecreatetruecolor($wb, $hb);
imagecopy($im_out, $im_b, 0, 0, 0, 0, $wb, $hb);
$destx = 372;
$desty = 645;


for($i = 0; $i < $wf; $i++) {
  for($j = 0; $j < $hf; $j++) {
    list($r, $g, $b) = getRGB($im_m, $i, $j);
    $alpha = $r / 255;

    list($fr, $fg, $fb) = getRGB($im_f, $i, $j);
    list($br, $bg, $bb) = getRGB($im_b, $i+$destx, $j+$desty);

    $outr = $alpha*$fr + (1 - $alpha)*$br;
    $outg = $alpha*$fg + (1 - $alpha)*$bg;
    $outb = $alpha*$fb + (1 - $alpha)*$bb;

    imagesetpixel($im_out, $i+$destx, $j+$desty, imagecolorallocate($im_out, $outr, $outg, $outb));
  }
}

imagepng($im_out, "result.png");

function getRGB($im, $i, $j) {
  $rgb = imagecolorat($im, $i, $j);
  $r = ($rgb >> 16) & 0xFF;
  $g = ($rgb >> 8) & 0xFF;
  $b = $rgb & 0xFF;
  return [$r, $g, $b];
}
