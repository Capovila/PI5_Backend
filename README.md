# Documentação API

Rotas e configurações da API

## Apêndice

criar um .venv pelo VsCode
caso na consiga entrar no venv, rode no terminal: source .venv/bin/activate

pip install Flask
pip install Supabase

## Documentação da API

Base URL: `http://localhost:3030`

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

**POST** `/api/alunos/`

| Corpo      | Tipo     |
| ---------- | -------- |
| `ra_aluno` | `number` |
| `nome`     | `string` |
| `id_turma` | `number` |

### Remover aluno

**DELETE** `/api/alunos/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar aluno

**PUT** `/api/alunos/:id`

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

**GET** `/api/disciplinas/area/:area_relacionada`

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

**POST** `/api/disciplinas/`

| Corpo              | Tipo     |
| ------------------ | -------- |
| `nome`             | `string` |
| `descricao`        | `string` |
| `semestre`         | `number` |
| `area_relacionada` | `string` |
| `ra_professor`     | `number` |

### Remover disciplina

**DELETE** `/api/disciplinas/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar disciplina

**PUT** `/api/disciplinas//:id`

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

**POST** `/api/professores/`

| Corpo          | Tipo      |
| -------------- | --------- |
| `ra_professor` | `number`  |
| `nome`         | `string`  |
| `email`        | `string`  |
| `senha`        | `string`  |
| `is_admin`     | `boolean` |
| `is_liberado`  | `boolean` |

### Remover professor

**DELETE** `/api/professores/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar professor

**PUT** `/api/professores/:id`

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

### Liberar professor

**PUT** `/api/professores/liberar/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Tornar professor administrador

**PUT** `/api/professores/admin/adicionar/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Remover professor como administrador

**PUT** `/api/professores/admin/remover/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

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

**POST** `/api/turmas/`

| Corpo         | Tipo                |
| ------------- | ------------------- |
| `data_inicio` | `date (yyyy-mm-dd)` |
| `isGraduated` | `boolean`           |

### Remover turma

**DELETE** `/api/turmas/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar turma

**PUT** `/api/turmas/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

| Corpo         | Tipo                |
| ------------- | ------------------- |
| `data_inicio` | `date (yyyy-mm-dd)` |
| `isGraduated` | `boolean`           |

### Graduar turma

**PUT** `/api/turmas/graduar/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

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

**POST** `/api/notas/`

| Corpo           | Tipo     |
| --------------- | -------- |
| `ra_aluno`      | `number` |
| `id_disciplina` | `number` |
| `nota`          | `number` |

### Remover nota

**DELETE** `/api/notas/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar nota

**PUT** `/api/notas/:id`

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

**POST** `/api/turma-disciplina/`

| Corpo            | Tipo      |
| ---------------- | --------- |
| `id_turma`       | `number`  |
| `id_disciplina`  | `number`  |
| `taxa_aprovacao` | `number`  |
| `isConcluida`    | `boolean` |

### Remover relação entre turma e disciplina

**DELETE** `/api/turma-disciplina/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

### Atualizar relação entre turma e disciplina

**PUT** `/api/turma-disciplina/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

| Corpo            | Tipo      |
| ---------------- | --------- |
| `id_turma`       | `number`  |
| `id_disciplina`  | `number`  |
| `taxa_aprovacao` | `number`  |
| `isConcluida`    | `boolean` |

### Concluir disciplina de uma turma

**PUT** `/api/turma-disciplina/concluir/:id`

| Parâmetro | Tipo     |
| --------- | -------- |
| `id`      | `number` |

---

Essa documentação fornece informações detalhadas sobre cada endpoint da API, padronizando a estrutura para melhor compreensão e manutenção.
