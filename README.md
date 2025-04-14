# Documentação API

Rotas e configurações da API

## Apêndice

Abrir arquivo .env e inserir seguintes campos

```
PASSWORD= senha do banco para o usuario
HOST= ip do banco (127.0.0.1 para localhost)
DATABASE= nome do database utilizado
LOCAL_USER= usuario utilizado
```

- npm i para instalar pacotes
- npm run dev para rodar backend

## Documentação da API

Base URL: `http://localhost:8080`

---

## Alunos

### Listar todos os alunos

**GET** `/api/alunos`

### Buscar aluno por ID

**GET** `/api/alunos/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Buscar alunos por turma

**GET** `/api/alunos/:turma`

| Parâmetro | Tipo     |
| --------- | -------- |
| `turma`   | `number` |

### Paginacao de alunos

**GET** `/api/alunos/pagination`

| Parâmetro | Tipo     |
| --------- | -------- |
| `page`    | `number` |
| `limit`   | `number` |

### Adicionar aluno

**POST** `/api/alunos/adicionar`

| Corpo      | Tipo     |
| ---------- | -------- |
| `ra_aluno` | `number` |
| `nome`     | `string` |
| `id_turma` | `number` |

### Remover aluno

**DELETE** `/api/alunos/delete/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar aluno

**PUT** `/api/alunos/patch/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

| Corpo      | Tipo     |
| ---------- | -------- |
| `nome`     | `string` |
| `id_turma` | `number` |

---

## Disciplinas

### Listar todas as disciplinas

**GET** `/api/disciplinas`

### Buscar disciplina por ID

**GET** `/api/disciplinas/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Buscar disciplinas por área

**GET** `/api/disciplinas/area`

| Corpo              | Tipo     |
| ------------------ | -------- |
| `area_relacionada` | `string` |

### Buscar disciplinas por semestre

**GET** `/api/disciplinas/semestre/:semestre`

| Parâmetro  | Tipo     |
| ---------- | -------- |
| `semestre` | `number` |

### Buscar disciplinas por RA do professor

**GET** `/api/disciplinas/ra/:ra`

| Parâmetro | Tipo     |
| --------- | -------- |
| `ra`      | `number` |

### Paginacao de disciplinas

**GET** `/api/disciplinas/pagination`

| Corpo   | Tipo     |
| ------- | -------- |
| `page`  | `number` |
| `limit` | `number` |

### Adicionar disciplina

**POST** `/api/disciplinas/adicionar`

| Corpo              | Tipo     |
| ------------------ | -------- |
| `nome`             | `string` |
| `descricao`        | `string` |
| `semestre`         | `number` |
| `area_relacionada` | `string` |
| `ra_professor`     | `number` |

### Remover disciplina

**DELETE** `/api/disciplinas/delete/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar disciplina

**PUT** `/api/disciplinas/patch/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

| Corpo              | Tipo     |
| ------------------ | -------- |
| `nome`             | `string` |
| `descricao`        | `string` |
| `semestre`         | `number` |
| `area_relacionada` | `string` |
| `ra_professor`     | `number` |

---

## Professores

### Listar todos os professores

**GET** `/api/professores`

### Buscar professor por ID

**GET** `/api/professores/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Paginacao de professores

**GET** `/api/professores/pagination`

| Parâmetro | Tipo     |
| --------- | -------- |
| `page`    | `number` |
| `limit`   | `number` |

### Adicionar professor

**POST** `/api/professores/adicionar`

| Corpo          | Tipo      |
| -------------- | --------- |
| `ra_professor` | `number`  |
| `nome`         | `string`  |
| `email`        | `string`  |
| `senha`        | `string`  |
| `is_admin`     | `boolean` |
| `is_liberado`  | `boolean` |

### Remover professor

**DELETE** `/api/professores/remove/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar professor

**PUT** `/api/professores/patch/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

| Corpo         | Tipo      |
| ------------- | --------- |
| `nome`        | `string`  |
| `email`       | `string`  |
| `senha`       | `string`  |
| `is_admin`    | `boolean` |
| `is_liberado` | `boolean` |

---

## Turmas

### Listar todas as turmas

**GET** `/api/turmas`

### Buscar turma por ID

**GET** `/api/turmas/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Buscar turma por data de início

**GET** `/api/turmas/data`

| Corpo         | Tipo                |
| ------------- | ------------------- |
| `data_inicio` | `date (yyyy-mm-dd)` |

### Paginação de turmas

**GET** `/api/turmas/pagination`

| Parâmetro | Tipo     |
| --------- | -------- |
| `page`    | `number` |
| `limit`   | `number` |

### Adicionar turma

**POST** `/api/turmas/adicionar`

| Corpo         | Tipo                |
| ------------- | ------------------- |
| `data_inicio` | `date (yyyy-mm-dd)` |
| `isGraduated` | `boolean`           |

### Remover turma

**DELETE** `/api/turmas/remove/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar turma

**PUT** `/api/turmas/patch/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

| Corpo         | Tipo                |
| ------------- | ------------------- |
| `data_inicio` | `date (yyyy-mm-dd)` |
| `isGraduated` | `boolean`           |

---

## Notas

### Listar todas as notas

**GET** `/api/notas`

### Buscar nota por ID

**GET** `/api/notas/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Buscar notas por ID da disciplina

**GET** `/api/notas/disciplina/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Buscar notas por ID do aluno

**GET** `/api/notas/aluno/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Paginação de notas

**GET** `/api/notas/pagination`

| Parâmetro | Tipo     |
| --------- | -------- |
| `page`    | `number` |
| `limit`   | `number` |

### Adicionar nota

**POST** `/api/notas/adicionar`

| Corpo           | Tipo     |
| --------------- | -------- |
| `ra_aluno`      | `number` |
| `id_disciplina` | `number` |
| `nota`          | `number` |

### Remover nota

**DELETE** `/api/notas/delete/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar nota

**PUT** `/api/notas/patch/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

| Corpo           | Tipo     |
| --------------- | -------- |
| `ra_aluno`      | `number` |
| `id_disciplina` | `number` |
| `nota`          | `number` |

---

## Relação Turma-Disciplina

### Listar todas as relações entre turmas e disciplinas

**GET** `/api/turma-disciplina`

### Buscar relação por ID

**GET** `/api/turma-disciplina/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Buscar todas as turmas que fazem uma disciplina específica

**GET** `/api/turma-disciplina/disciplina/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Buscar todas as disciplinas de uma turma específica

**GET** `/api/turma-disciplina/turma/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Adicionar relação entre turma e disciplina

**POST** `/api/turma-disciplina/adicionar`

| Corpo            | Tipo      |
| ---------------- | --------- |
| `id_turma`       | `number`  |
| `id_disciplina`  | `number`  |
| `taxa_aprovacao` | `number`  |
| `isConcluida`    | `boolean` |

### Remover relação entre turma e disciplina

**DELETE** `/api/turma-disciplina/delete/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar relação entre turma e disciplina

**PUT** `/api/turma-disciplina/patch/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

| Corpo            | Tipo      |
| ---------------- | --------- |
| `id_turma`       | `number`  |
| `id_disciplina`  | `number`  |
| `taxa_aprovacao` | `number`  |
| `isConcluida`    | `boolean` |

---

Essa documentação fornece informações detalhadas sobre cada endpoint da API, padronizando a estrutura para melhor compreensão e manutenção.
