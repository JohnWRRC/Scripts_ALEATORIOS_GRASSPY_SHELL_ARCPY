setwd("D:/Pessoas/John")

setwd("txts")
arquivos=list.files()
Narquivos=length(arquivos)
lista.orig=list()

same.as.GRASS=T

for(i in 1:Narquivos) {
	lista.orig[[i]]=read.table(arquivos[i],sep="",header=F)
	}

names(lista.orig) = arquivos

setwd("..")
setwd("temp")

for(i in 1:Narquivos) {
	write.table(lista.orig[[i]],file=arquivos[i], quote=F, row.names=F, col.names=F, sep="=")
	}

lista.working=list()

for(i in 1:Narquivos) {
	lista.working[[i]]=read.table(arquivos[i],sep="=",header=F, stringsAsFactors=F)
	}

names(lista.working) = arquivos

lista.final=list()

for(i in 1:Narquivos) {
	lista.final[[i]] = lista.working[[i]][,-1][,c(F,T)]
	colnames(lista.final[[i]]) = lista.working[[i]][1,-1][c(T,F)]
	}

file.remove(arquivos)


setwd("..")

setwd("final")


for(i in 1:Narquivos) {
	foo=lista.final[[i]]
	
	if(same.as.GRASS){
		for(j in 1:ncol(foo)) {
			foo[,j][is.na(foo[,j])] = ""
			foo[,j]=paste(colnames(foo)[j],"=",foo[,j],sep="")
			}
		
		write.table(foo, file=arquivos[i],quote=F, row.names=F, col.names=F, sep=" ", na=" ")
		} else write.table(foo, file=arquivos[i],quote=F, row.names=F, col.names=T, sep="\t", na="NA")
	}













