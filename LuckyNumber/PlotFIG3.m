clear; clc;
figure;
ha = tight_subplot(2, 2,[.1 .1],[.2 .1],[.15 .1]);
set(gcf,'color','white');
set(gcf, 'Position', [500 300 800 500]);

load('./data/2013~2018各项变化率.mat');

axes(ha(1));  % friends
h1=plot(a1(:,1), 1-a1(:,3)./(a1(:,2)+a1(:,3)), '-', 'Color', [0, 0.5, 0], 'LineWidth', 3);
legend(h1, 'friends', 'location', 'NW');
set(legend, 'box', 'off', 'FontName', 'Times New Roman', 'FontSize', 14);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16)

axes(ha(2));  % followers
h2=plot(a2(:,1), 1-a2(:,3)./(a2(:,2)+a2(:,3)), 'm-', 'LineWidth', 3);
legend(h2, 'follwers', 'location', 'NW');
set(legend, 'box', 'off', 'FontName', 'Times New Roman', 'FontSize', 14);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16)

axes(ha(3));  % posts
h3=plot(a3(:,1), 1-a3(:,3)./(a3(:,2)+a3(:,3)), '-', 'Color', [0.93, 0.69, 0.13], 'LineWidth', 3);
legend(h3, 'posts', 'location', 'NW');
set(legend, 'box', 'off', 'FontName', 'Times New Roman', 'FontSize', 14);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16)

axes(ha(4));  % location
h4=plot(a4(:,1), 1-a4(:,3)./(a4(:,2)+a4(:,3)), 'c-', 'LineWidth', 3);
legend(h4, 'geo-loc', 'location', 'NW');
set(legend, 'box', 'off', 'FontName', 'Times New Roman', 'FontSize', 14);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16)



