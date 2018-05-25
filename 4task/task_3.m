close all;
clear all;

A = imread('./cameraman.tif');

% zerando DC
F1 = fft2(double(A));
F1(1,1) = 0;
I1 = ifft2(F1);

% subtraindo intensidade média
I2 = imread('./cameraman.tif');
I2 = I2 - mean2(I2);

subplot(1, 3, 1), imshow(A, []), title("Original");
subplot(1, 3, 2), imshow(I1, []), title("zerando DC");
subplot(1, 3, 3), imshow(I2, []), title("subtraindo intensidade média");