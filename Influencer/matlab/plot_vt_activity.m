function plot_vt_activity()
s = 'D:\Projects\Pycharm\BIGV\data\bigv\vt_fans_activity\';
A = [];
normal = load(strcat(s, '-1')); A = [A mean(normal)];
celebrity = load(strcat(s, '0')); A = [A mean(celebrity)];
government = load(strcat(s, '1')); A = [A mean(government)];
enterprise = load(strcat(s, '2')); A = [A mean(enterprise)];
media = load(strcat(s, '3')); A = [A mean(media)];
school = load(strcat(s, '4')); A = [A mean(school)];
website = load(strcat(s, '5')); A = [A mean(website)];
organization = load(strcat(s, '7')); A = [A mean(organization)];
weibo_lady = load(strcat(s, '10')); A = [A mean(weibo_lady)];
junior_talent = load(strcat(s, '200')); A = [A mean(junior_talent)];
senior_talent = load(strcat(s, '220')); A = [A mean(senior_talent)];

figure;
subplot(1, 2, 1);
x1 = {'Government','Junior talent','Enterprise', 'Weibo lady', 'Media', ...
    'Senior talent', 'Organization', 'School', 'Website', 'Normal', 'Celebrity'};
y1 = sort(A); 
barh(y1, 'c');
title('$Fans Activity$', 'interpreter', 'Latex');
xlim([0, 0.5]);
set(gca, 'yticklabel', x1, 'Fontname', 'Times New Roman');
set(gca, 'FontSize', 15);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);
hold on

subplot(1, 2, 2);
data1 = load('D:\Projects\Pycharm\BIGV\data\verified_type');
L = data1(:, 3);
T = tabulate(L); T = T(:, 3) ./ 100;
y2 = [T(3), T(10), T(4), T(9), T(5), T(11), T(8), T(6), T(7), T(1), T(2)];
barh(y2, 'y');
title('$Distribution$', 'interpreter', 'Latex');
xlim([0, 0.7]);
set(gca, 'yticklabel', x1, 'Fontname', 'Times New Roman');
set(gca, 'FontSize', 15);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);
