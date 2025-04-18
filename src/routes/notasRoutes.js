import express from "express";
import * as notasController from "../controllers/notasController.js";

const router = express.Router();

router.get("/", notasController.getNotas);
router.get("/pagination", notasController.getNotasPagination);
router.get("/:id", notasController.getNotasById);
router.get("/aluno/:id", notasController.getNotasByAlunoId);
router.get("/disciplina/:id", notasController.getNotasByDisciplinaId);

router.post("/", notasController.addNotas);

router.delete("/:id", notasController.deleteNotas);

router.put("/:id", notasController.patchNotas);

export default router;
