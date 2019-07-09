clear; clc;
figure;
ha = tight_subplot(1, 2,[.1 .1],[.1 .1],[.1 .1]);
set(gcf,'color','white');
set(gcf, 'Position', [500 300 800 500]);

axes(ha(1));
load('./data/follower_distribution_on_luckynumber_s_following.mat');
x=a(:,1); y=a(:,2)/sum(a(:,2));
semilogx(x, y, 'b.');
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',18);
axes('position',[0.15,0.35,0.1,0.2]);
semilogx(x, y, 'r.');
xlim([10 1000]); ylim([0 0.0002]);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16);

axes(ha(2));
load('./data/follower_distribution_on_unluckynumber_s_following.mat');
x=a(:,1); y=a(:,2)/sum(a(:,2));
semilogx(x, y, '.', 'Color', [0.75, 0, 0.75]);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',18);
axes('position',[0.61,0.35,0.1,0.2]);
semilogx(x, y, 'c.');
xlim([10 1000]); ylim([0 0.0003]);
set(gca, 'box', 'on', 'LineWidth', 1.2, 'FontName', 'Times New Roman', 'FontSize',16);


