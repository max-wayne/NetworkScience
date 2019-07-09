clear; clc;
figure;
[~,~,rewdata]=xlsread('./data/test2.xlsx');
x=1:34;
for i=20:20:20*34
    y(i)=rewdata{i/20,4}*100-0.7161;
end
bar(y,16);
axis([0 700 -0.1 0.5]);
set(gca,'xtick',[])
ylabel('Deviation');
for i=20:20:20*23
    text(i,-0.08,rewdata{i/20,5},'rotation',90,'fontsize',15);
end
for i=20*24:20:20*34
    text(i,0.01,rewdata{i/20,5},'rotation',90,'fontsize',15);
end
set(gca,'yticklabel',{'-0.1%','0.72%','+0.1%','+0.2%','+0.3%','+0.4%','+0.5%'},'fontsize',20)
set(gcf,'Units','centimeters','Position',[6 3 21 13]);
% saveas(gcf,'4.fig');