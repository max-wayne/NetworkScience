clear; clc;

figure;
ha = tight_subplot(1, 3,[.1 .1],[.1 .1],[.15 .1]);
set(gcf,'color','white');
set(gcf, 'Position', [500 300 1000 400]);

axes(ha(1));
load('./data/GDPandBFB.mat');
x=bfb(1:31); y=gdp(1:31);
plot(x, y, '.', 'Color', [0.75, 0.75, 0], 'MarkerSize', 30);
ylabel('Capital GDP($)');
xlim([0.5 1.3]); ylim([0 20000]);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16);

axes(ha(2));
load('./data/education&BFB.mat');
x=a; y=b(:,1);
plot(x, y, '.', 'Color', [0.31, 0.31, 0.31], 'MarkerSize', 30);
ylabel('Capital Education(years)');
xlim([0.5 1.3]); ylim([3 15]);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16);

axes(ha(3));
load('./data/education&BFB.mat');
x=a; y=b(:,2);
plot(x, y, '.', 'Color', [1, 0.6, 0.78], 'MarkerSize', 30);
ylabel('Proportion of Higher Education');
xlim([0.5 1.3]); ylim([0 0.5]);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16);

