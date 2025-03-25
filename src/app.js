import express from "express";
import cors from "cors";

import turmasRoutes from "./routes/turmasRoutes.js";
import alunosRoutes from "./routes/alunosRoutes.js";
import disciplinasRoutes from "./routes/disciplinasRoutes.js";
import notasRoutes from "./routes/notasRoutes.js";
import professoresRoutes from "./routes/professoresRoutes.js";
import turmaDisciplinaRoutes from "./routes/turmaDisciplinaRoutes.js";

const app = express();
app.use(express.json());
app.use(cors());

app.use(" /turmas", turmasRoutes);
app.use("/alunos", alunosRoutes);
app.use("/disciplinas", disciplinasRoutes);
app.use("/notas", notasRoutes);
app.use("/professores", professoresRoutes);
app.use("/turmaDisciplina", turmaDisciplinaRoutes);

export default app;
