movie_list=[("오징어게임",50.45), ("이터널스", 35.46), ("그레비티", 9.8), ("노타임투다이", 52.5), ("스파이더맨", 15.47)]

movie_list=sorted(movie_list, key=lambda x:x[1], reverse=True)
movie= dict(movie_list)

print("영화제목","\t\t","예매율","\t","순위")
print("="*8,"\t\t","="*6,"\t","="*4)

r=0
for i, j in movie.items():
    r=r+1
    print(f"{i} \t\t {j} \t\t {r}")
