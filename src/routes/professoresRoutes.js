import express from "express";
import * as professoresController from "../controllers/professoresController.js";

const router = express.Router();

router.get("/", professoresController.getProfessores);
router.get("/pagination", professoresController.getProfessoresPagination);
router.get("/:id", professoresController.getProfessoresById);

router.post("/adicionar", professoresController.addProfessores);

router.delete("/delete/:id", professoresController.deleteProfessor);

router.put("/patch/:id", professoresController.patchProfessor);
router.put("/liberar/:id", professoresController.liberarProfessor);
router.put("/admin/remover/:id", professoresController.removerProfessorAdmin);
router.put("/admin/adicionar/:id", professoresController.tornarProfessorAdmin);

export default router;
