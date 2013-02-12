
x = 0:0.001:1;

x0 = 0;

x1 = 1;

L0 = (x-x1)/(x0-x1);

L1 = (x-x0)/(x1-x0);


plot(x,L0,x,L1,'-.');

axis([-0.1,0.1,0,1.1]);

format_ticks(gca,{'$x_0$','$x_1$'},{'$1$'},[0,1],1);

legend('L_0','L_1','Location','East')