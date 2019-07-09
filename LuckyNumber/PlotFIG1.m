clear; clc;
figure;
load('./data/distribution.mat');
semilogx([201 201], [0 1.6e-3], '--', 'Color', [0.49, 0.18, 0.56], 'LineWidth', 2.5); hold on;
semilogx(a(:,1),a(:,2)/sum(a(:,2)), '-', 'Color', [0.47, 0.67, 0.19], 'LineWidth', 3);

xlabel('Number of friends');
ylabel('Distribution');
xlim([50 1000]); ylim([0 6e-3]);
set(gcf,'color','white');
set(gcf, 'Position', [500 300 800 500]);
set(gca, 'box', 'on', 'LineWidth', 1.5, 'FontName', 'Times New Roman', 'FontSize',20);


