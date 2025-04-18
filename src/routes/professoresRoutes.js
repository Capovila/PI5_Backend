import express from "express";
import * as professoresController from "../controllers/professoresController.js";

const router = express.Router();

router.get("/", professoresController.getProfessores);
router.get("/pagination", professoresController.getProfessoresPagination);
router.get("/:id", professoresController.getProfessoresById);

router.post("/", professoresController.addProfessores);

router.delete("/:id", professoresController.deleteProfessor);

router.put("/:id", professoresController.patchProfessor);
router.put("/liberar/:id", professoresController.liberarProfessor);
router.put("/admin/:id", professoresController.professorAdmin);

export default router;
