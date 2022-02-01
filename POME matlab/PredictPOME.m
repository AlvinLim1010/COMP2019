function output=PredictPOME(FILE_PATH,NN_FILE_PATH,numOfRows)
load(NN_FILE_PATH,'net');
rowRecord=(numOfRows-1)+3;
range=strcat('C3:S',num2str(rowRecord));
data=readtable(FILE_PATH,'Range',range);

pomeAttribute=data;
pomeAttribute(:,[7,11,14,17])=[];
pomeAttribute=rmmissing(pomeAttribute);
pomeAttribute=[pomeAttribute(:,5:13) pomeAttribute(:,2:3) pomeAttribute(:,1)];
pomeAttribute=table2array(pomeAttribute);

organised_data=[pomeAttribute(:,1:9)];
organised_data=transpose(organised_data);

out=sim(net,organised_data);
output=transpose(out);
end