pkg load image;
clear;
close all;
fclose all;
%%
imglist = '../list/img_list.txt';
list = textread(imglist, '%s');
output_root = '../edges';
%vis_output_root = '../edges_vis';

human_inst_root = fullfile('../images');



for i = 1:length(list);
    imname = list{i};
    img_rbg = imread(fullfile(human_inst_root, [imname '.jpg']));
    img_gray = rgb2gray(img_rbg);
    instance_contour = uint8(imgradient(img_gray) > 0);
        
        
    imwrite(instance_contour, fullfile(output_root, [imname '.png']));
%    imwrite(instance_contour*255, fullfile(vis_output_root, [imname '.png']));


end    
