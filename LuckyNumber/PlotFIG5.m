clear; clc;
figure;
ha = tight_subplot(1, 2,[.1 .1],[.1 .1],[.15 .1]);
set(gcf,'color','white');
set(gcf, 'Position', [500 300 800 500]);

axes(ha(1));
load('./data/ratio_of_yuanc_zhuanf.mat');
x=a(:,1)./(a(:,1)+a(:,2));
[m,n]=hist(x); 
h1=bar(n, m/sum(m));
set(h1, 'FaceColor', 'green', 'EdgeColor', 'green');
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',20);

axes(ha(2));
load('./data/ratio_of_yuanc_zhuanf2.mat');
x=a(:,1)./(a(:,1)+a(:,2));
[m,n]=hist(x); 
h2=bar(n, m/sum(m));
set(h2, 'FaceColor', 'yellow', 'EdgeColor', 'yellow');
ylim([0 0.15]);
set(gca, 'YTick', [0, 0.05, 0.1, 0.15], 'YTickLabel', {'0', '0.05', '0.1', '0.15'});
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',20);

