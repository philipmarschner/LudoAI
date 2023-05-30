close all
file_paths = [
      "agn_10_gms_200_gen_500_mut_0.01_mutS_0.05_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.01_mutS_0.1_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.01_mutS_0.2_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.01_mutS_0.5_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.05_mutS_0.05_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.05_mutS_0.1_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.05_mutS_0.2_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.05_mutS_0.5_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.1_mutS_0.05_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.1_mutS_0.1_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.1_mutS_0.2_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.1_mutS_0.5_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.2_mutS_0.05_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.2_mutS_0.1_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.2_mutS_0.2_el_0.1.csv";...
      "agn_10_gms_200_gen_500_mut_0.2_mutS_0.5_el_0.1.csv"];

for i  = 1:16
    [generation_id, win_rates, chromosome] = importfile(file_paths(i));
    gen_ids(i,:,:) = generation_id;
    wr_ids(i,:,:) = win_rates;
    chrom_ids(i,:,:,:) = chromosome;
    temp_maks =max(win_rates,[],2);
    maks(i) = temp_maks(end);
    temp_gns = mean(win_rates,2);
    gns(i) = temp_gns(end);
    fig = figure;
    plot(min(win_rates,[],2))
    hold on
    plot(mean(win_rates,2))
    plot(max(win_rates,[],2))
    xlabel('Generation')
    ylabel('Win rate')
    legend(["min","mean","max"],"Location","southeast")
    grid on
    title("Mut rate: %, Mut size: %")
    set(gcf,'units','points','position',[500,500,200,150])
end
%%

figure
maks2d(1,:) = maks(1:4);
maks2d(2,:) = maks(5:8);
maks2d(3,:) = maks(9:12);
maks2d(4,:) = maks(13:16);
maks2d = maks2d*100;
xvalues = {'5','10','20','50'};
yvalues = {'1','5','10','20'};
m = heatmap(xvalues,yvalues,maks2d);
m.Title = 'Max fitness [%]';
m.XLabel = 'Mutation Size [%]';
m.YLabel = 'Mutation Rate [%]';
set(gcf,'units','points','position',[500,500,200,150])
exportgraphics(m,'maks2.pdf','BackgroundColor','none')

%%
figure
gns2d(1,:) = gns(1:4);
gns2d(2,:) = gns(5:8);
gns2d(3,:) = gns(9:12);
gns2d(4,:) = gns(13:16);
gns2d = gns2d*100;
xvalues = {'5','10','20','50'};
yvalues = {'1','5','10','20'};
m = heatmap(xvalues,yvalues,gns2d);
m.Title = 'Mean fitness [%]';
m.XLabel = 'Mutation Size [%]';
m.YLabel = 'Mutation Rate [%]';
set(gcf,'units','points','position',[500,500,200,150])
exportgraphics(m,'mean2.pdf','BackgroundColor','none')

%%
[generation_id, win_rates, chromosome] = importfile("agn_10_gms_200_gen_500_mut_0.1_mutS_0.5_el_0.1.csv");
fig = figure;
plot(min(win_rates,[],2))
hold on
plot(mean(win_rates,2))
plot(max(win_rates,[],2))
xlabel('Generation')
ylabel('Win rate')
legend(["min","mean","max"],"Location","south")
grid on
title("Mut rate: 10%, Mut size: 50%")
set(gcf,'units','points','position',[500,500,200,150])
exportgraphics(fig,'best.pdf','BackgroundColor','none')

%%
[generation_id, win_rates, chromosome] = importfile("agn_10_gms_200_gen_500_mut_0.01_mutS_0.05_el_0.1.csv");
fig = figure;
plot(min(win_rates,[],2))
hold on
plot(mean(win_rates,2))
plot(max(win_rates,[],2))
ylim([0,0.6]);
xlabel('Generation')
ylabel('Win rate')
legend(["min","mean","max"],"Location","north")
grid on
title("Mut rate: 1%, Mut size: 5%")
set(gcf,'units','points','position',[500,500,200,150])
exportgraphics(fig,'worst.pdf','BackgroundColor','none')

%%
[generation_id, win_rates, chromosome] = import_50("agn_50_gms_200_gen_250_mut_0.1_mutS_0.5_el_0.1.csv");
fig = figure;
plot(min(win_rates,[],2))
hold on
plot(mean(win_rates,2))
plot(max(win_rates,[],2))
xlabel('Generation')
ylabel('Win rate')
legend(["min","mean","max"],"Location","south")
grid on
title("Mut rate: 10%, Mut size: 50%")
set(gcf,'units','points','position',[500,500,200,150])
exportgraphics(fig,'bestlong.pdf','BackgroundColor','none')