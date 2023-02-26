
alunos = (
    ('Érica', 16, 2021),
    ('Pedro Vinícius', 17, 2021),
    ('Geovana',17,2021),
    ('Marcos',18,2021)
)

print(list(enumerate(alunos)))

idades = []

for aluno, idade, ano_entrada in alunos:
    idades.append(idade)
    print(aluno)

idades.reverse()
print(idades)