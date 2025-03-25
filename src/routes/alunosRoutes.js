import express from "express";
import * as alunosController from "../controllers/alunosController.js";

const router = express.Router();

router.get("/", alunosController.getAlunos);
router.get("/:id", alunosController.getAlunosById);

export default router;
