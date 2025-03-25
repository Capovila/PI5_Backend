import express from "express";
import * as disciplinasController from "../controllers/disciplinasController.js";

const router = express.Router();

router.get("/", disciplinasController.getAlunos);
router.get("/:id", disciplinasController.getAlunosById);

export default router;
