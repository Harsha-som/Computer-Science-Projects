# Data types
a <- c(2.3, -3.0, 0)
b<-c(1L,-3L,10L)
typeof(d)
d<-c("apple", "pear", "peach") #combined function 
rm(c)
l<-c(T,F,T) #these are reserved words 
d[c(2,3)]


#Convert data type, temporary
as.integer(a)
as.character(b)
as.double(b)

#Mixing datatypes 
m<-c(1L,2.3,T, "peach")
2<"03" #converts 2 to "2" and then copares 2 to 0 first, False
2<"3" #converts 2 to "2" and then compares 2 to 3, True

#Data structure 
df<-data.frame(first_column=a,second=b,third=d,fourth=l)
df[2,1:4]
df[2,c(1,2,3,4)]
df["fourth"]
l2<-df$fourth
df$e<-c(5,7,-1)
df$f<-"a"
str(df) #structure to see data type in df


#List
lst<-list(a=2.3, b=df, c=a)
lst$c[3]
x<-lst[2] #output is 1 component list
class(x)
x$b$third
y<-lst[[2]] #output is content of the component 
class(y)

#Factors
dat<- PlantGrowth
boxplot(weight~group, dat)
f<-dat$group
attributes(f)
levels(f)
dat$group<-factor(dat$group, levels=c("trt1","trt2","ctrl"))

dat1<-subset(dat,group!="ctrl")
boxplot(weight~group,dat1)
levels(dat1$group)
dat1$group<-droplevels(dat1$group)




