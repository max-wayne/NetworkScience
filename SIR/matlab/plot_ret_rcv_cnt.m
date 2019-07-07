function plot_ret_rcv_cnt(f, d)
%% plot all ret_rcv_cnt.
file = strcat('D:/double_check/info/filename_', f, '.txt');
fid = fopen(file, 'r'); ret_rcv_cnt = [];
figure(); hold on;
while ~feof(fid)
    s = fgetl(fid);
    p = strcat('D:/double_check/info/', s, '/res');
    load(p); trunc = length(t2(:, 3));
    if trunc >= d
        a = t2(1:d, 3)./100; 
    else
        a = t2(:, 3); a(trunc+1 : d) = 0; a = a./100;
    end
    ret_rcv_cnt = [ret_rcv_cnt; a'];
end
fclose(fid);
%%
x = 1 : d;
bar(x, mean(ret_rcv_cnt));
xlabel('$ReceivedTimesBeforeRetweet$', 'Interpreter', 'LaTeX');
ylabel('$Distribution$', 'Interpreter', 'LaTeX');
set(gcf,'color', 'white');
set(gca, 'LineWidth', 1, 'FontName', 'Times New Roman', 'FontSize',20);
aaa = mean(ret_rcv_cnt);
disp(cumsum(aaa)./sum(aaa));
